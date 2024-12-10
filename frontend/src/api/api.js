import axios from 'axios';
import Cookies from "js-cookie";

const apiUrl = 'http://localhost:5000/api/v1';

// Axios instance for handling requests
const axiosInstance = axios.create({
    baseURL: apiUrl,
    headers: {
        'Content-Type': 'application/json',
    },
});


export const getAllUsers = async () => {
    try {
        const response = await axiosInstance.get('/users');
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const loginUser = async (credentials) => {
    try {
        const response = await axiosInstance.post('/login', credentials);
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const registerUser = async (userData) => {
    try {
        const response = await axiosInstance.post('/register', userData);
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const logoutUser = async () => {
    try {
        const response = await axiosInstance.post('/logout',
            {
                headers: {
                    Authorization: `Bearer ${Cookies.get("token")}`,
                },
            }
        );
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const forgotPassword = async (email) => {
    try {
        const response = await axiosInstance.post('/forgot-password', { email });
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const resetPassword = async (data) => {
    try {
        const response = await axiosInstance.post('/reset-password', data);
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const getUserProfile = async () => {
    try {
        const response = await axiosInstance.get('/profile');
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const updateUserProfile = async (profileData) => {
    try {
        const response = await axiosInstance.put('/profile', profileData);
        return response.data;
    } catch (error) {
        throw error;
    }
};

export const checkIsAuthenticated = () => {
    const token = Cookies.get("token");
    return token ? true : false;
  };
