import React, { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';
import LoaderDash from '../components/loader/loaders-dashboard';
import { checkIsAuthenticated } from '../api/api';
import { useToast } from '@chakra-ui/react';

export const ProtectedRoute = ({ children } : { children: React.ReactNode }) => {
  const [authenticated, setAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const toast = useToast();

  useEffect(() => {
    const checkToken = async () => {
      try {
        setLoading(true);
        const token = checkIsAuthenticated();
        setAuthenticated(!!token);
      } catch (err) {
        toast({
          title: 'Error',
          description: 'An error occurred while checking for authentication.',
          status: 'error',
          duration: 9000,
          isClosable: true,
          position: 'top'
        });
      } finally {
        setLoading(false);
      }
    };

    checkToken();
  }, [toast]);

  if (loading) {
    return <LoaderDash />;
  } else if (authenticated) {
    return children;
  } else {
    return <Navigate to='/login' replace />;
  }
};