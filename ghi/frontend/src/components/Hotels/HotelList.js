import React, { useState, useEffect } from 'react';

function HotelList(){
    const [hotels, setHotels] = useState([]);

    const getHotels = async () => {
        const url = 'http://localhost:8000/friendly_agent/hotels/';
        const response = await fetch(url);

        if (response.ok){
            const data = await response.json();
            const hotels = data.hotels;
            setHotels(hotels);
            console.log(hotels);
        }
    };
    useEffect(() => {
        getHotels();
    }, []);

    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Hotel Details</th>
                    <th>Hotel Name</th>
                    <th>City</th>
                    <th>Country</th>
                    <th>Check In Date</th>
                    <th>Check Out Date</th>
                    <th>Number of Travelers</th>
                    <th>Total Cost</th>
                </tr>
            </thead>
            <tbody>
                {hotels.map((hotel) => {
                    return (
                        <tr key={hotel.id}>
                            <td>{hotel.hotel_details}</td>
                            <td>{hotel.hotel_name}</td>
                            <td>{hotel.hotel_city}</td>
                            <td>{hotel.hotel_country}</td>
                            <td>{hotel.check_in_date}</td>
                            <td>{hotel.check_out_date}</td>
                            <td>{hotel.hotel_number_of_guests}</td>
                            <td>{hotel.hotel_total_cost}</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>
    )
}

export default HotelList;