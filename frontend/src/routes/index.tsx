import {
  RouterProvider
} from 'react-router-dom';
import { router } from './router';
import React from 'react';

export const Router = () => {
  return (
    <RouterProvider router={router} />
  );
}
;