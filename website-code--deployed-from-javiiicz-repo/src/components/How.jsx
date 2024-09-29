import demo from "../assets/demo.gif"

function How() {
    return (
        <div id="how" className="p-[5%] my-20 bg-[#F8F3F8]">
            <div data-aos="fade-right">
                <h3 className="text-3xl font-bold underline underline-offset-2 decoration-violet-500">How It Works</h3>
                
                <ol className="text-lg list-decimal px-12 py-4 space-y-4">
                    <li><span className="font-bold">Facial Detection:</span> The program captures video from the driver's webcam and detects facial landmarks using a pre-trained model.</li>
                    <li><span className="font-bold">Eye and Mouth Analysis:</span>
                        <ul className="list-disc px-8">
                            <li><span className="font-bold">Eye Aspect Ratio (EAR)</span>: The program calculates the eye aspect ratio to determine whether the eyes are open or closed. If both eyes are closed for a specified duration, it indicates potential drowsiness.</li>
                            <li><span className="font-bold">Mouth Aspect Ratio (MAR)</span>: It analyzes mouth movements to detect yawning, another sign of fatigue.</li>
                        </ul>
                    </li>
                    <li><span className="font-bold">Alerts</span>:
                        <ul className="list-disc px-8">
                            <li>When signs of drowsiness are detected (e.g., prolonged eye closure or frequent yawning), the program displays a "DROWSINESS ALERT!" message on the screen.</li>
                            <li>An auditory alert is triggered, notifying the driver to take a break.</li>
                        </ul>
                    </li>
                    <li><span className="font-bold">Real-time Monitoring</span>: The system continuously processes video frames, updating the driver’s eye and mouth status, ensuring immediate responses to fatigue signs.</li>
                </ol>
                <div className="flex justify-center">
                    <img src={demo} className="rounded"></img>
                </div>
            </div>
        </div>
    )
}

export default How;