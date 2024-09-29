import group from "../assets/group.jpg"

function Next() {
    return (
        <div id="next" className="p-[5%]">
            <div data-aos="fade-up" data-aos-offset="0">
                <h3 className="text-3xl font-bold underline underline-offset-2 decoration-violet-500 text-center">What's Next</h3>
                <div className="flex justify-center py-5 text-xl text-center">
                <p className="w-[70%]">In the future, we aim to make DrowsyDriver accessible to everyone. With more time, we envision developing a compact device that can be easily mounted on dashboards, catering to concerned family members, friends, and truck drivers alike. Additionally, we plan to gather data from this device to create an application that alerts family members about their loved ones’ safety. Our goal is to enhance road safety and ensure peace of mind for all users.</p>
                </div>
                
                <div className="flex justify-center my-8">
                    <img src={group} alt="Group photo of the hackers" className="w-[80%] rounded"></img>
                </div>
            </div>
        </div>
    )
}

export default Next;