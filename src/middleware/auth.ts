/**
 * @file auth.ts
 * @description High-priority implementation of JWT authentication middleware 
 * for the nTrust Dashboard API (Task #1).
 */

import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

// Environment variable for secret key, falling back to a dev default
const SECRET_KEY = process.env.JWT_SECRET || 'ntrust-internal-secret-key-dev';

export interface AuthenticatedRequest extends Request {
  user?: any; // In production, this would be typed as UserPayload
}

/**
 * Middleware to verify JWT tokens on incoming requests.
 * Blocks execution if token is missing or invalid.
 */
export const authenticateToken = async (req: AuthenticatedRequest, res: Response, next: NextFunction): Promise<void> => {
  const authHeader = req.headers['authorization'];
  
  // Extract the bearer token from "Bearer <token>"
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    res.status(401).json({ message: 'Access denied. No token provided.' });
    return;
  }

  try {
    // Verify the token
    const decoded = jwt.verify(token, SECRET_KEY) as { id: string; role: string };
    
    // Attach user data to the request object for downstream use
    req.user = decoded;
    next();
  } catch (err) {
    res.status(403).json({ message: 'Invalid or expired token.' });
  }
};

/**
 * Middleware to check specific roles.
 */
export const authorizeRole = (...roles: string[]) => {
  return (req: AuthenticatedRequest, res: Response, next: NextFunction) => {
    if (!req.user || !roles.includes(req.user.role)) {
      res.status(403).json({ message: 'Forbidden: Insufficient permissions.' });
      return;
    }
    next();
  };
};
