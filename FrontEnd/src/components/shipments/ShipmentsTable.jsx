import React, { useEffect } from "react";
import { fetchShipments } from "../../stores/api"; // Adjust the correct path
import shipmentsStore from "../../stores/useStore"; // Adjust the correct path

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
            <th>رقم الشحنة</th>
            <th>اسم السائق</th>
            <th>اسم العميل</th>
            <th>المصدر</th>
            <th>الوجهه</th>
            <th>التحميل</th>
            <th>الوصول</th>
            <th>الاجرة</th>
            <th>حالة الشحنة</th>
          </tr>
        </thead>
        <tbody>
          {shipments.map((shipment) => (
            <tr key={shipment.id}>
              <td>{shipment.id}</td>
              <td>{shipment.driver.name}</td>
              <td>{shipment.customer_branch.customers.name}</td>{" "}
              {/* Accessing customer name */}
              <td>{shipment.customer_branch.city}</td>
              <td>{shipment.destination.name_ar}</td>
              <td>
                {new Date(shipment.created_at)
                  .toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "2-digit",
                    day: "2-digit",
                  })
                  .replace(/(\d{2})\/(\d{2})\/(\d{4})/, "$3/$1/$2")}
              </td>
              <td>
                {new Date(shipment.actual_delivery_date)
                  .toLocaleDateString("en-US", {
                    year: "numeric",
                    month: "2-digit",
                    day: "2-digit",
                  })
                  .replace(/(\d{2})\/(\d{2})\/(\d{4})/, "$3/$1/$2")}
              </td>
              <td>{shipment.fare}</td>
              <td>
                <button
                  className={`btn ${
                    shipment.status === "Shipped"
                      ? "btn-warning"
                      : shipment.status === "Delivered"
                      ? "btn-success"
                      : shipment.status === "Late"
                      ? "btn-danger"
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
