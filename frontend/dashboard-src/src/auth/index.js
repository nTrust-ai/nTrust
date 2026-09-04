/**
 * index.js — Auth & Session Management module barrel export (Weaver deliverable 2026-09-04)
 * Supports: TASK-58B692, TASK-6D2960, TASK-B31DEE, TASK-1D1912
 */
export { AuthProvider, useAuth } from './AuthContext';
export { authService } from './authService';
export { LoginForm } from './LoginForm';
export { LogoutButton } from './LogoutButton';
export { RouteGuard } from './RouteGuard';
export { UserProfileCard } from './UserProfileCard';
