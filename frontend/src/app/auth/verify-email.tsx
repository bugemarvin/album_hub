import { Box, Flex } from "@chakra-ui/react";
import React from "react";

export const VerifyEmail = () => {
  return (
    <>
      <Flex
        justify="center"
        align="center"
        h="100vh"
        w={"100%"}
        position={"relative"}
      >
        <Box>
          <h1>Verify Email</h1>
          <p>Check your email for a link to verify your email address.</p>
        </Box>
      </Flex>
    </>
  );
};
