import React, { useEffect } from "react";
import { fetchShipments } from "../stores/api";
import shipmentsStore from "../stores/useStore";

const ShipmentsList = () => {
  const { shipments, setShipments } = shipmentsStore();

  useEffect(() => {
    fetchShipments().then(setShipments);
  }, [setShipments]); // Added dependency array to avoid infinite loop

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Driver Name</th>
            <th>Customer Branch</th>
            <th>Destination</th>
            <th>ID</th>
            <th>Status</th>
            <th>Actual Delivery Date</th>
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
                <button className="btn btn-success">
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
