import React from "react";
import {
  Box,
  Flex,
  Heading,
  Text,
  Stack,
  Container,
  Avatar,
  useColorModeValue
} from "@chakra-ui/react";

interface Props {
  children: React.ReactNode;
}

const Testimonial = (props: Props) => {
  const { children } = props;

  return <Box>{children}</Box>;
};

const TestimonialContent = (props: Props) => {
  const { children } = props;

  return (
    <Stack
      bg={useColorModeValue("white", "gray.800")}
      boxShadow={"lg"}
      p={8}
      rounded={"xl"}
      align={"center"}
      pos={"relative"}
      _after={{
        content: `""`,
        w: 0,
        h: 0,
        borderLeft: "solid transparent",
        borderLeftWidth: 16,
        borderRight: "solid transparent",
        borderRightWidth: 16,
        borderTop: "solid",
        borderTopWidth: 16,
        borderTopColor: useColorModeValue("white", "gray.800"),
        pos: "absolute",
        bottom: "-16px",
        left: "50%",
        transform: "translateX(-50%)"
      }}
    >
      {children}
    </Stack>
  );
};

const TestimonialHeading = (props: Props) => {
  const { children } = props;

  return (
    <Heading as={"h3"} fontSize={"xl"} color={'primary.400'}>
      {children}
    </Heading>
  );
};

const TestimonialText = (props: Props) => {
  const { children } = props;

  return (
    <Text
      textAlign={"center"}
      color={useColorModeValue("gray.600", "gray.400")}
      fontSize={"sm"}
    >
      {children}
    </Text>
  );
};

const TestimonialAvatar = ({
  src,
  name,
  title
}: {
  src: string;
  name: string;
  title: string;
}) => {
  return (
    <Flex align={"center"} mt={8} direction={"column"}>
      <Avatar src={src} mb={2} />
      <Stack spacing={-1} align={"center"}>
        <Text fontWeight={600} color={'primary.400'}>{name}</Text>
        <Text fontSize={"sm"} color={useColorModeValue("gray.600", "gray.400")}>
          {title}
        </Text>
      </Stack>
    </Flex>
  );
};

export default function Testimonials() {
  return (
    <Box>
      <Container maxW={"7xl"} py={16} as={Stack} spacing={12}>
        <Stack spacing={0} align={"center"}>
          <Heading color={'primary.400'}>What Our <span className="text-gray-700">Users Say</span></Heading>
          <Text>
            Hear how AlbumHub has transformed workflows for photographers,
            content creators, and teams worldwide.
          </Text>
        </Stack>
        <Stack
          direction={{ base: "column", md: "row" }}
          spacing={{ base: 10, md: 4, lg: 10 }}
        >
          <Testimonial>
            <TestimonialContent>
              <TestimonialHeading><span className="text-gray-700">Streamlined</span> My Workflow</TestimonialHeading>
              <TestimonialText>
                AlbumHub has completely revolutionized the way I manage my
                projects. The intuitive interface and fast performance make my
                day so much easier."
              </TestimonialText>
            </TestimonialContent>
            <TestimonialAvatar
              src={
                "https://plus.unsplash.com/premium_photo-1688740375397-34605b6abe48?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              }
              name={"Jessica Tran"}
              title={"Professional Photographer"}
            />
          </Testimonial>
          <Testimonial>
            <TestimonialContent>
              <TestimonialHeading>
              <span className="text-gray-700">Perfect for</span> Team Collaboration
              </TestimonialHeading>
              <TestimonialText>
                Our team uses AlbumHub to organize and share media collections.
                The secure login and responsive design make it easy to work from
                anywhere.
              </TestimonialText>
            </TestimonialContent>
            <TestimonialAvatar
              src={
                "https://plus.unsplash.com/premium_photo-1689568126014-06fea9d5d341?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              }
              name={"Daniel Kim"}
              title={"Marketing Manager"}
            />
          </Testimonial>
          <Testimonial>
            <TestimonialContent>
              <TestimonialHeading>
              <span className="text-gray-700">Incredibly Simple</span> and Effective
              </TestimonialHeading>
              <TestimonialText>
                I’ve tried other platforms, but AlbumHub stands out for its
                simplicity and reliability. It’s a must-have for managing large
                photo libraries.
              </TestimonialText>
            </TestimonialContent>
            <TestimonialAvatar
              src={
                "https://plus.unsplash.com/premium_photo-1688350839154-1a131bccd78a?q=80&w=1738&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
              }
              name={"Aisha Mohammed"}
              title={"Content Creator"}
            />
          </Testimonial>
        </Stack>
      </Container>
    </Box>
  );
}
