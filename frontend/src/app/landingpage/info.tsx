import React from "react";
import {
  Box,
  Heading,
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  Text,
  Container
} from "@chakra-ui/react";
import { ChevronDownIcon } from "@chakra-ui/icons";

export default function Info() {
  return (
    <Box
      textAlign="center"
      py={10}
      px={6}
      gap={4}
      alignItems={"center"}
      display={"flex"}
      flexDirection={"column"}
    >
      <Heading as="h2" size="xl" mt={6} mb={2}>
        Why AlbumHub is <span className="text-primary-400">Right for You</span>
      </Heading>
      <Text color={"gray.500"}>
        Choose AlbumHub for its unmatched efficiency, user-friendly interface,
        and versatile functionality. Perfect for individuals and teams managing
        diverse media collections.
      </Text>
      <Container
        display={"flex"}
        flexDirection={"column"}
        alignItems={"center"}
      >
        <Accordion allowMultiple width="100%" minW="4xl" rounded="lg">
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}
            >
              <Text fontSize="md">Effortless Media Organization</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
                With AlbumHub, you can easily navigate and manage users, albums,
                and photos without hassle.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}
            >
              <Text fontSize="md">User-Centric Design</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
                The platform is designed with simplicity and functionality in
                mind, making it perfect for both individuals and teams.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}
            >
              <Text fontSize="md">Flexibility Across Devices</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
                Whether you’re at your desk or on the go, AlbumHub adapts to
                your screen size and ensures a seamless experience.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}
            >
              <Text fontSize="md">Real-Time Updates</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
                Make edits and see changes instantly, thanks to AlbumHub’s
                efficient real-time synchronization.
              </Text>
            </AccordionPanel>
          </AccordionItem>
          <AccordionItem>
            <AccordionButton
              display="flex"
              alignItems="center"
              justifyContent="space-between"
              p={4}
            >
              <Text fontSize="md">Built for Modern Needs</Text>
              <ChevronDownIcon fontSize="24px" />
            </AccordionButton>
            <AccordionPanel pb={4}>
              <Text color="gray.600">
                From secure authentication to lightning-fast performance,
                AlbumHub has everything you need to streamline your media
                management..
              </Text>
            </AccordionPanel>
          </AccordionItem>
        </Accordion>
      </Container>
    </Box>
  );
}
