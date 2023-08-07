import React, { useState, useEffect } from 'react';

function FlightList() {
    const [flights, setFlights] = useState([]);

    const getFlights = async () => {
        const url = 'http://localhost:8000/friendly_agent/flights/';
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            const flights = data.flights;
            setFlights(flights);
            console.log(flights);
        }
    }
    useEffect(() => {
        getFlights();
    }, []);

    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Flight Details</th>
                    <th>Airline</th>
                    <th>Departure City</th>
                    <th>Departure Airport</th>
                    <th>Arrival City</th>
                    <th>Arrival Airport</th>
                    <th>Layover</th>
                    <th>Departure Time</th>
                    <th>Arrival Time</th>
                    <th>Number of Travelers</th>
                    <th>Total Cost</th>
                </tr>
            </thead>
            <tbody>
                {flights.map((flight) => {
                    return (
                        <tr key={flight.id}>
                            <td>{flight.flight_details}</td>
                            <td>{flight.airline}</td>
                            <td>{flight.departure_city}</td>
                            <td>{flight.departure_airport}</td>
                            <td>{flight.arrival_city}</td>
                            <td>{flight.arrival_airport}</td>
                            <td>{flight.layover}</td>
                            <td>{flight.departure_time}</td>
                            <td>{flight.arrival_time}</td>
                            <td>{flight.flight_number_of_travelers}</td>
                            <td>{flight.flight_total_cost}</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>


    )




}

export default FlightList;