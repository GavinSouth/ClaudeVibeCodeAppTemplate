import '@testing-library/jest-dom/vitest'
import { cleanup } from '@testing-library/react'
import { afterEach } from 'vitest'

// Unmount after every test (automatic only when Vitest globals are on, which we don't use).
afterEach(cleanup)
