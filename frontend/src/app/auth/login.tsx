import React, { useState } from "react";
import {
  Flex,
  Box,
  FormControl,
  FormLabel,
  Input,
  Checkbox,
  Stack,
  Button,
  Heading,
  Text,
  useColorModeValue,
  InputGroup,
  InputRightElement
} from "@chakra-ui/react";
import { Link } from "react-router-dom";
import { ViewIcon, ViewOffIcon } from "@chakra-ui/icons";

export function Login() {
  const [showPassword, setShowPassword] = useState(false);
  return (
    <Flex
      minH={"100vh"}
      align={"center"}
      justify={"center"}
      bg={useColorModeValue("gray.50", "gray.800")}
    >
      <Stack spacing={8} mx={"auto"} maxW={"lg"} py={12} px={6}>
        <Stack align={"center"}>
          <Heading fontSize={"4xl"}>Sign in to your account</Heading>
          <Text fontSize={"lg"} color={"gray.600"} w={'max-content'}>
            to enjoy all of our cool <span className="text-primary-400">features</span> ✌️
          </Text>
        </Stack>
        <Box
          rounded={"lg"}
          bg={useColorModeValue("white", "gray.700")}
          boxShadow={"lg"}
          p={8}
        >
          <Stack spacing={4}>
            <FormControl id="email">
              <FormLabel>Email address</FormLabel>
              <Input type="email" focusBorderColor="primary.400"/>
            </FormControl>
            <FormControl id="password">
              <FormLabel>Password</FormLabel>
              {/* <Input type="password" focusBorderColor="primary.400"/> */}
              <InputGroup>
                <Input type={showPassword ? "text" : "password"} focusBorderColor="primary.400"/>
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
            <Stack spacing={10}>
              <Stack
                direction={{ base: "column", sm: "row" }}
                align={"start"}
                justify={"space-between"}
              >
                <Checkbox
                  colorScheme="primary"
                  defaultChecked={false}
                  color="gray.700"
                >
                  Remember me
                </Checkbox>
                <Link
                  to="/reset-email"
                  color="primary"
                  className="hover:text-primary-400 text-primary"
                >
                  Forgot password?
                </Link>
              </Stack>
              <Button
                bg={"primary.400"}
                color={"white"}
                _hover={{
                  bg: "primary.500"
                }}
              >
                Sign in
              </Button>
            </Stack>
            <Stack pt={6}>
              <Text align={"center"}>
                Don't have an account?{" "}
                <Link
                  to="/register"
                  color="primary"
                  className="hover:text-primary-400 text-primary"
                >
                  Register
                </Link>
              </Text>
            </Stack>
          </Stack>
        </Box>
      </Stack>
    </Flex>
  );
}
