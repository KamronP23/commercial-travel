import React, { useState, useEffect } from 'react';

function PackageList(){
    const [packages, setPackages] = useState([]);

    const getPackages = async () => {
        const url = 'http://localhost:8000/friendly_agent/packages/';
        const response = await fetch(url);

        if (response.ok){
            const data = await response.json();
            const packages = data.packages;
            setPackages(packages);
            console.log(packages);
        }
    }
    useEffect(() => {
        getPackages();
    }, []);

    return(
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Trip Name</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Total Cost</th>
                    <th>Total Travelers</th>
                </tr>
            </thead>
            <tbody>
                {packages.map((package1) => {
                    return (
                        <tr key={package1.id}>
                            <td>{package1.trip_name}</td>
                            <td>{package1.start_date}</td>
                            <td>{package1.end_date}</td>
                            <td>{package1.package_total_cost}</td>
                            <td>{package1.total_travelers}</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>

    )

}

export default PackageList;