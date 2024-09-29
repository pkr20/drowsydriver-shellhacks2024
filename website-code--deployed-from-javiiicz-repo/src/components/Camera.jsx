import React, { useRef, useState, useEffect } from 'react';

const Camera = () => {

    const handleButtonClick = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/execute', {
                method: 'POST', // Use POST to call the endpoint
                headers: {
                    'Content-Type': 'application/json', 
                    'Access-Control-Allow-Origin': '*'// Specify the content type
                },
                body: JSON.stringify({ /* any data you want to send */ }), // Send data if needed
            });
    
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
    
            const data = await response.json();
            console.log('Response from Flask:', data);
        } catch (error) {
            console.error('Error:', error);
        }
    };
    return (
        <div data-aos="zoom-in" className='flex flex-row items-center justify-center p-[5%]'>
            <div onClick={handleButtonClick} className='cursor-pointer text-center text-5xl text-white font-bold bg-gray-800 px-40 py-28 rounded-[100px] hover:bg-violet-500 transition-all shadow'>
                Try it Out
            </div>
        </div>
    );
};

export default Camera;
