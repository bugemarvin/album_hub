import React, { useState } from "react";
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  InputGroup,
  HStack,
  InputRightElement,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  useToast,
} from "@chakra-ui/react";
import { ViewIcon, ViewOffIcon } from "@chakra-ui/icons";
import { Link, useNavigate } from "react-router-dom"; // Import useNavigate for redirection
import { registerUser } from "../../api/api"; // Adjust the path according to your file structure
import Cookies from "js-cookie"; // Import Cookies from js-cookie

export function Register() {
  const [showPassword, setShowPassword] = useState(false);
  const [userData, setUserData] = useState({
    username: "",
    email: "",
    password: "",
    password_confirm: "",
  });
  const toast = useToast();
  const history = useNavigate(); // Initialize history for redirection

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Check if passwords match
    if (userData.password !== userData.password_confirm) {
      toast({
        title: "Passwords do not match",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
      return;
    }

    try {
      const response = await registerUser(userData);

      // Check if the response indicates success
      if (response.success) {
        const token = response.data.token;

        // Set token in cookies using js-cookie
        Cookies.set("token", token, { expires: 7, path: "/" });

        // Redirect to dashboard
        history("/dashboard");

        toast({
          title: "Registration successful!",
          description: response.message,
          status: "success",
          duration: 3000,
          isClosable: true,
          position: "top-right",
        });
      } else {
        toast({
          title: "Registration failed",
          description: response.message || "An error occurred.",
          status: "error",
          duration: 3000,
          isClosable: true,
          position: "top-right",
        });
      }
    } catch (error) {
      toast({
        title: "Registration failed",
        description: error.response?.data?.message || "Something went wrong.",
        status: "error",
        duration: 3000,
        isClosable: true,
      });
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUserData({ ...userData, [e.target.id]: e.target.value });
  };

  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
        <Stack align={"center"}>
          <Heading fontSize={"4xl"} textAlign={"center"}>
            Sign up
          </Heading>
          <Text fontSize={"lg"} color={"gray.600"}>
            to enjoy all of our cool features ✌️
          </Text>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <form onSubmit={handleSubmit}>
              <HStack>
                <Box>
                  <FormControl id="username" isRequired>
                    <FormLabel>First Name</FormLabel>
                    <Input
                      type="text"
                      focusBorderColor="primary.400"
                      onChange={handleChange}
                      value={userData.username}
                    />
                  </FormControl>
                </Box>
              </HStack>
              <FormControl id="email" isRequired>
                <FormLabel>Email address</FormLabel>
                <Input
                  type="email"
                  onChange={handleChange}
                  value={userData.email}
                  focusBorderColor="primary.400"
                />
              </FormControl>
              <FormControl id="password" isRequired>
                <FormLabel>Password</FormLabel>
                <InputGroup>
                  <Input
                    type={showPassword ? "text" : "password"}
                    focusBorderColor="primary.400"
                    onChange={handleChange}
                    value={userData.password}
                  />
                  <InputRightElement h={"full"}>
                    <Button
                      variant={"ghost"}
                      onClick={() =>
                        setShowPassword((showPassword) => !showPassword)
                      }
                    >
                      {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                    </Button>
                  </InputRightElement>
                </InputGroup>
              </FormControl>
              <FormControl id="password_confirm" isRequired>
                <FormLabel>Confirm Password</FormLabel>
                <InputGroup>
                  <Input
                    type={showPassword ? "text" : "password"}
                    focusBorderColor="primary.400"
                    onChange={handleChange}
                    value={userData.password_confirm}
                  />
                  <InputRightElement h={"full"}>
                    <Button
                      variant={"ghost"}
                      onClick={() =>
                        setShowPassword((showPassword) => !showPassword)
                      }
                    >
                      {showPassword ? <ViewIcon /> : <ViewOffIcon />}
                    </Button>
                  </InputRightElement>
                </InputGroup>
              </FormControl>
              <Stack spacing={10} pt={2}>
                <Button
                  type="submit"
                  loadingText="Submitting"
                  size="lg"
                  bg={"primary.400"}
                  color={"white"}
                  _hover={{
                    bg: "primary.500",
                  }}
                >
                  Sign up
                </Button>
              </Stack>
            </form>
            <Stack pt={6}>
              <Text align={"center"}>
                Already a user?{" "}
                <Link
                  to="/login"
                  color="primary"
                  className="hover:text-primary-400 text-primary"
                >
                  Login
                </Link>
              </Text>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
