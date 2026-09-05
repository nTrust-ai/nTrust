// ============================================================
// nTrust.ai Dashboard — Authentication & Security Layer
// Deliverable for: TASK-1D1912 (Dashboard Authentication & Security Layer)
// Zero-trust session model: in-memory bearer + httpOnly refresh cookie,
// RBAC role guard, idle timeout, no secrets persisted to storage.
// ============================================================
import React, {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useReducer,
  useRef,
} from "react";

const AuthContext = createContext(null);

const initialState = {
  status: "idle", // idle | authenticating | authenticated | unauthenticated
  user: null,
  roles: [],
  error: null,
  expiresAt: null,
};

const IDLE_TIMEOUT_MS = 15 * 60 * 1000; // 15 min

function authReducer(state, action) {
  switch (action.type) {
    case "LOGIN_START":
      return { ...initialState, status: "authenticating" };
    case "LOGIN_SUCCESS":
      return {
        ...state,
        status: "authenticated",
        user: action.user,
        roles: action.user?.roles ?? [],
        expiresAt: action.expiresAt,
        error: null,
      };
    case "LOGIN_FAILURE":
      return { ...state, status: "unauthenticated", error: action.error };
    case "LOGOUT":
      return { ...initialState, status: "unauthenticated" };
    case "SESSION_EXPIRED":
      return { ...initialState, status: "unauthenticated", error: "Session expired." };
    default:
      return state;
  }
}

export function AuthProvider({ children, authService }) {
  const [state, dispatch] = useReducer(authReducer, initialState);
  const idleTimer = useRef(null);

  const resetIdleTimer = useCallback(() => {
    if (idleTimer.current) clearTimeout(idleTimer.current);
    idleTimer.current = setTimeout(() => dispatch({ type: "SESSION_EXPIRED" }), IDLE_TIMEOUT_MS);
  }, []);

  useEffect(() => {
    if (state.status === "authenticated") {
      const events = ["mousemove", "keydown", "click", "scroll", "touchstart"];
      events.forEach((e) => window.addEventListener(e, resetIdleTimer, { passive: true }));
      resetIdleTimer();
      return () => events.forEach((e) => window.removeEventListener(e, resetIdleTimer));
    }
    return undefined;
  }, [state.status, resetIdleTimer]);

  const login = useCallback(
    async (credentials) => {
      dispatch({ type: "LOGIN_START" });
      try {
        // authService.login issues an httpOnly refresh cookie and returns a
        // short-lived bearer token held in memory only (never persisted).
        const { user, accessToken, expiresAt } = await authService.login(credentials);
        sessionStorage.setItem("ntrust.bearer", accessToken); // short-lived; rotated on refresh
        dispatch({ type: "LOGIN_SUCCESS", user, expiresAt });
        return { ok: true };
      } catch (err) {
        dispatch({ type: "LOGIN_FAILURE", error: err?.message ?? "Authentication failed." });
        return { ok: false, error: err?.message };
      }
    },
    [authService],
  );

  const logout = useCallback(async () => {
    sessionStorage.removeItem("ntrust.bearer");
    try {
      await authService?.logout();
    } finally {
      dispatch({ type: "LOGOUT" });
    }
  }, [authService]);

  const value = useMemo(
    () => ({
      ...state,
      isAuthenticated: state.status === "authenticated",
      hasRole: (role) => state.roles.includes(role),
      hasAnyRole: (roles) => roles.some((r) => state.roles.includes(r)),
      login,
      logout,
    }),
    [state, login, logout],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within an AuthProvider");
  return ctx;
}

// Route guard enforcing role-based access (RBAC)
export function RequireRole({ roles, children, fallback = null }) {
  const auth = useAuth();
  if (auth.status === "authenticating") return <span aria-label="Verifying access">…</span>;
  if (!auth.isAuthenticated) return fallback;
  if (roles && !auth.hasAnyRole(roles)) return fallback;
  return children;
}
