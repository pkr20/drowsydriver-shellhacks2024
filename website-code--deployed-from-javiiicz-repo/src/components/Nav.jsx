import React from "react"
import logo from "../assets/logo.svg"

function Nav() {
    return (
        <div className="h-16 w-full flex flew-row items-center bg-gray-100/50 z-50 gap-4 sticky top-0 backdrop-blur-md px-16 shadow-sm">
            <a className="flex flex-row items-center cursor-pointer" href="#top">
                <img src={logo} alt="Sleepy face emoji outline" className="h-full p-2"></img>
                <h1 className='text-3xl font-bold drop-shadow' >DrowsyDriver</h1>
            </a>
            <div className="flex flex-row justify-end w-full gap-4">
                <a className="cursor-pointer hover:font-medium transition-all" href="#intro">Intro</a>
                <a className="cursor-pointer hover:font-medium transition-all" href="#how">How</a>
                <a className="cursor-pointer hover:font-medium transition-all" href="#next">What's Next</a>
                <a className="cursor-pointer hover:font-medium transition-all" href="#us">About us</a>
            </div>
        </div>
    )
}

export default Nav