import React from "react";
import Navigation from "./navigation";
import HeroSection from "./hero";
import Features from "./features";
import Testimonials from "./testimonials";
import Footer from "./footer";
import Info from "./info";
import Statistics from "./statistics";
import Contact from "./contact-page";

export const LandingPage = () => {
  return (
    <>
      <div>
          <Navigation />
          <HeroSection />
          <Features />
          <Statistics />
          <Testimonials />
          <Info />
          <Contact />
          <Footer />
      </div>
    </>
  );
};
