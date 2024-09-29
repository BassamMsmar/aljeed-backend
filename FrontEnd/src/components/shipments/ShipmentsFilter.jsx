import { useEffect, useState } from "react";
import { fetchUsers, fetchCustomers, fetchStatus } from "../../stores/api"; // Adjust the correct path
import shipmentsStore from "../../stores/useStore";

const ShipmentsFilter = () => {
  const [
    users,
    setUsers,
    customers,
    setCustomers,
    shipmentStatus,
    setShipmentStatus,
    filters,
    setFilters,
  ] = shipmentsStore((state) => [
    state.users,
    state.setUsers,
    state.customers,
    state.setCustomers,
    state.shipmentStatus,
    state.setShipmentStatus,
    state.filters,
    state.setFilters,
  ]);

  useEffect(() => {
    fetchUsers().then(setUsers); // Fetch users and update the store
  }, [setUsers]);

  useEffect(() => {
    fetchCustomers().then(setCustomers); // Fetch customers and update the store
  }, [setCustomers]);

  useEffect(() => {
    fetchStatus().then(setShipmentStatus); // Fetch customers and update the store
  }, [setShipmentStatus]);

  const handleUserChange = (e) => {
    const { value, checked } = e.target;
    const newUser = checked
      ? [...filters.selectedUsers, parseInt(value)]
      : filters.selectedUsers.filter((user) => user !== parseInt(value));

    setFilters({ ...filters, selectedUsers: newUser });
  };
  // const handlecustomersChange
  // const handleshipmentStatus

  return (
    <div className="user-id-status-container">
      <h3>المستخدمين</h3>

      <div>
        {users.map((user) => (
          <div
            key={user.id}
            className="btn-group mb-2 mx-1"
            role="group"
            aria-label="Basic checkbox toggle button group"
            style={{ width: "100px" }} // Set a fixed width for equal size
          >
            <input
              type="checkbox"
              className="btn-check"
              id={user.id}
              autoComplete="off"
              value={user.id}
              onChange={handleUserChange}
            />
            <label
              className="btn btn-outline-primary btn-sm"
              htmlFor={user.id}
              style={{ width: "100px", textAlign: "center" }}
            >
              {user.first_name} - {user.id}
            </label>
          </div>
        ))}
      </div>

      <h3>العملاء</h3>
      <div>
        {customers.map((customer) => (
          <div
            key={customer.id}
            className="btn-group mb-2 mx-1"
            role="group"
            aria-label="Basic checkbox toggle button group"
            style={{ width: "100px" }} // Set a fixed width for equal size
          >
            <input
              type="checkbox"
              className="btn-check"
              id={`btncheck${customer.id}`}
              autoComplete="off"
            />
            <label
              className="btn btn-outline-primary btn-sm"
              htmlFor={`btncheck${customer.id}`}
              style={{ width: "100px", textAlign: "center" }}
            >
              {customer.customers.name} {" - "} {customer.name}
            </label>
          </div>
        ))}
      </div>

      <h3>حالة الشحنة</h3>
      <div>
        {shipmentStatus.map((status) => (
          <div
            key={status.id}
            className="btn-group mb-2 mx-1"
            role="group"
            aria-label="Basic checkbox toggle button group"
            style={{ width: "100px" }} // Set a fixed width for equal size
          >
            <input
              type="checkbox"
              className="btn-check"
              id={status.id}
              autoComplete="off"
            />
            <label
              // className="btn btn-outline-primary btn-sm "
              className={`btn ${
                status.name_en === "Shipped"
                  ? "btn-outline-warning"
                  : status.name_en === "Delivered"
                  ? "btn-outline-success"
                  : status.name_en === "Late"
                  ? "btn-outline-danger"
                  : "btn-outline-secondary"
              }`}
              htmlFor={status.id}
              style={{ width: "100px", textAlign: "center" }}
            >
              {status.name_ar}
            </label>
          </div>
        ))}
      </div>

      <h3>التاريخ</h3>
    </div>
  );
};

export default ShipmentsFilter;
