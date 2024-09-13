import React from "react";
import "./TableStyles.css"; // Import your custom styles
import { useEffect } from "react";

import { fetchShipments } from "../stores/api";
import shipmentsStore from "../stores/useStore";

const ShipmentsList = () => {
  const { shipments, setShipments } = shipmentsStore();

  useEffect(() => {
    fetchShipments().then(setShipments);
  });

  const getStatusClass = (status) => {
    switch (status) {
      case "In Transit":
        return "status-in-transit";
      case "Completed":
        return "status-completed";
      case "Delayed":
        return "status-delayed";
      default:
        return "";
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Shipment Information</h2>
      <table className="table table-responsive-md table-bordered table-striped table-hover">
        <thead className="thead-dark">
          <tr>
            <th>Driver Name</th>
            <th>Branch Name</th>
            <th>Destination</th>
            <th>Shipment Number</th>
            <th>Status</th>
            <th>Delivery Date</th>
            <th>Fare</th>
            <th>Premium</th>
          </tr>
        </thead>
        <tbody>
          {shipments.map((shipment) => (
            <tr key={shipment.id}>
              <td>{shipment.driver.name}</td>
              <td>
                {shipment.customer_branch.name} -{" "}
                {shipment.customer_branch.city}
              </td>
              <td>
                {shipment.destination.name_ar} ({shipment.destination.name_en})
              </td>
              <td>{shipment.id}</td>
              <td>
                <button
                  className="btn btn-success"
                >
                  {shipment.status}
                </button>
              </td>
              <td>
                {new Date(shipment.actual_delivery_date).toLocaleDateString()}
              </td>
              <td>{shipment.fare}</td>
              <td>{shipment.premium}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ShipmentsList;
