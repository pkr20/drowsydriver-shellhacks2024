import React from 'react';
import javi from '../assets/javi.jpeg'
import joshy from '../assets/yoshy.png'
import kayleen from '../assets/kayleen.jpeg'
import alans from "../assets/alan.png"

const AboutUs = () => {
  return (
    <div id="us" className="py-16 bg-cover bg-bottom bg-white/20">
      <div className= "mx-auto text-center">
        <h2 className="text-4xl font-bold mb-8 underline underline-offset-2 decoration-violet-500">About Us</h2>
        <p className="text-lg mb-12">
          We are a team of passionate individuals from the University of Miami committed to making a difference in road safety.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="flex flex-col items-center">
            <div className="w-32 h-32 rounded-full overflow-hidden mb-4">
              <img
                src={kayleen}
                alt="Team Member 1"
                className="w-full h-full object-cover"
              />
            </div>
            <h3 className="text-xl font-semibold">Kayleen Ramirez</h3>
            
          </div>
          <div className="flex flex-col items-center">
            <div className="w-32 h-32 rounded-full overflow-hidden mb-4">
              <img
                src={javi}
                alt="Team Member 2"
                className="w-full h-full object-cover"
              />
            </div>
            <h3 className="text-xl font-semibold">Javier Carrillo</h3>
            
          </div>
          <div className="flex flex-col items-center">
            <div className="w-32 h-32 rounded-full overflow-hidden mb-4">
              <img
                src={alans}
                alt="Team Member 3"
                className="w-full h-full object-cover"
              />
            </div>
            <h3 className="text-xl font-semibold">Alans Fuentes</h3>
            
          </div>
          <div className="flex flex-col items-center">
            <div className="w-32 h-32 rounded-full overflow-hidden mb-4">
              <img
                src={joshy}
                alt="Team Member 4"
                className="w-full h-full object-cover"
              />
            </div>
            <h3 className="text-xl font-semibold">Joshua Yepes</h3>
            
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
