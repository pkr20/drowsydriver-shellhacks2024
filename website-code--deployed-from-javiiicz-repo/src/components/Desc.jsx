import drive from "../assets/drive.jpeg"

function Desc() {
    return (
      <div id="intro" className="flex items-center justify-around mt-52 bg-gray-50/20 mx-[5%] p-8 rounded-xl" data-aos="fade-right">
          <div className="sm:px-20 py-2 text-lg flex sm:flex-row flex-col gap-5 items-center">
            <div className="sm:w-[60%]">
                <span className="font-bold text-2xl underline underline-offset-2 decoration-violet-500">Introducing Drowsy Driver</span>, an innovative software solution designed to enhance your camera's capabilities by monitoring driver fatigue in real-time. This lightweight application utilizes advanced, accessible facial recognition algorithms to efficiently analyze drivers' facial features and eye movements, detecting signs of drowsiness before it's too late. With instant alerts sent to the driver, Drowsy Driver ensures safer driving experiences while significantly reducing the risk of accidents caused by fatigue. Transform your standard camera into a powerful safety tool—make every journey safer and more secure with Drowsy Driver!
            </div>
            <div>
                <img src={drive} className="w-80 h-80 object-cover rounded" alt="A person driving at night">
                </img>
            </div>
          </div>
      </div>
    );
  }
  
  export default Desc;
  