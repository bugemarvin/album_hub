import React from "react";
import {
  Box,
  Container,
  Heading,
  SimpleGrid,
  Icon,
  Text,
  Stack,
  HStack,
  VStack
} from "@chakra-ui/react";
import { CheckIcon } from "@chakra-ui/icons";

// Replace test data with your own
const features = [
  {
    id: 1,
    title: "User Profiles Made Easy",
    text: "Quickly browse and manage user profiles with seamless integration."
  },
  {
    id: 2,
    title: "Album Organization",
    text: "Organize and explore albums with user-specific details and stats."
  },
  {
    id: 3,
    title: "Photo Editing on the Go",
    text: "Edit photo titles instantly and sync updates in real-time."
  },
  {
    id: 4,
    title: "Mobile-First Design",
    text: "Enjoy a responsive experience across all devices—mobile, tablet, or desktop."
  }
];

export default function Features() {
  return (
    <Box p={4}>
      <Stack spacing={4} as={Container} maxW={"3xl"} textAlign={"center"}>
        <Heading fontSize={"3xl"} color={'primary.400'}>Explore What <span className="text-gray-700">AlbumHub Offers</span></Heading>
        <Text color={"gray.600"} fontSize={"xl"}>
          From user profiles to detailed photo editing, AlbumHub empowers you
          with tools to manage your media effortlessly. Designed for reliability
          and flexibility, it's your ultimate media management companion.
        </Text>
      </Stack>

      <Container maxW={"6xl"} mt={10}>
        <SimpleGrid columns={{ base: 1, md: 2, lg: 4 }} spacing={10}>
          {features.map((feature) => (
            <HStack key={feature.id} align={"top"}>
              <Box color={"primary.400"} px={2}>
                <Icon as={CheckIcon} />
              </Box>
              <VStack align={"start"}>
                <Text fontWeight={600} color={'gray.700'}>{feature.title}</Text>
                <Text color={"gray.600"}>{feature.text}</Text>
              </VStack>
            </HStack>
          ))}
        </SimpleGrid>
      </Container>
    </Box>
  );
}
