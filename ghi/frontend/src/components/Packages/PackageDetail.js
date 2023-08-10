import React, { useState, useEffect } from 'react';
import {useParams, useNavigate} from 'react-router-dom';

function PackageDetail() {
    const [package1, setPackage] = useState({});
    const { id } = useParams();
    const navigate = useNavigate();

    async function getPackage(package_id) {
        try {
            const url = `http://localhost:8000/friendly_agent/packages/${package_id}/`;
            const response = await fetch(url);

            if (response.ok) {
                const data = await response.json();
                setPackage(data);
                console.log(data)
            }
        } catch(error) {
            console.log("No Package Detected");
        }
    }

    useEffect(() => {
        getPackage(id);
    }, [id]);
    return (
        <div className="row">
            <div className="col-md-7 col-lg-3">
                <div className="card-body pt-0">
                <h4 className="card-title"><strong>Package Details</strong></h4>
                    <p></p>
                    <p className="card-text"><strong>Package Name: </strong>{package1.trip_name}</p>
                    <p className="card-text"><strong>Start Date: </strong>{package1.start_date}</p>
                    <p className="card-text"><strong>End Date: </strong>{package1.end_date}</p>
                    <p className="card-text"><strong>Total Travelers: </strong>{package1.clients && package1.clients.length}</p>
                    <p className="card-text"><strong>Package Cost: </strong>{package1.package_total_cost}</p>
                    <p className="card-text">
                        <strong>Clients: </strong>
                        {package1.clients &&
                            package1.clients
                                .map(client => `${client.first_name} ${client.last_name}`)
                                .sort((a, b) => a.localeCompare(b))
                                .join(", ")}
                    </p>
                    <p className="card-text">
                        <strong>Groups: </strong>
                        {package1.groups &&
                            package1.groups.map(group => group.group_name).join(", ")}
                    </p>
                    <p className="card-text">
                        <strong>Flights: </strong>
                        {package1.flights &&
                            package1.flights.map(flight => flight.flight_details).sort().join(", ")}
                    </p>
                    <p className="card-text">
                        <strong>Hotels: </strong>
                        {package1.hotels &&
                            package1.hotels.map(hotel => hotel.hotel_details).join(", ")}
                    </p>
                    <p className="card-text">
                        <strong>Cruises: </strong>
                        {package1.cruises &&
                            package1.cruises.map(cruise => cruise.cruise_details).join(", ")}
                    </p>
                    <button onClick={() => navigate('/packages')}>Back</button>
                </div>
            </div>
        </div>
    )
}

export default PackageDetail;