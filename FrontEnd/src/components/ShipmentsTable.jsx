import React, { useEffect } from "react";
import { fetchShipments } from "../stores/api"; // استخدام المسار الصحيح للملف
import shipmentsStore from "../stores/useStore"; // استخدام المسار الصحيح للملف

const ShipmentsList = () => {
  const { shipments, setShipments } = shipmentsStore();

  useEffect(() => {
    fetchShipments().then(setShipments);
  }, [setShipments]);

  const ShipmentsTable = ({ shipments }) => (
    <div className="container mt-4">
      <table className="table table-striped table-bordered table-hover">
        <thead className="thead-dark">
          <tr>
            <th>Driver Name</th>
            <th>Customer Branch</th>
            <th>Destination</th>
            <th>ID</th>
            <th>Actual Delivery Date</th>
            <th>Fare</th>
            <th>Premium</th>
            <th>Status</th>
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
                {new Date(shipment.actual_delivery_date).toLocaleDateString()}
              </td>
              <td>{shipment.fare.toFixed(2)}</td>
              <td>{shipment.premium.toFixed(2)}</td>
              <td>
                <button
                  className={`btn ${
                    shipment.status === "Completed"
                      ? "btn-success"
                      : shipment.status === "Delayed"
                      ? "btn-warning"
                      : "btn-secondary"
                  }`}
                >
                  {shipment.status}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  return <ShipmentsTable shipments={shipments} />;
};

export default ShipmentsList;
