import { useEffect, useState } from "react";
import { fetchUsers, fetchCustomers } from "../../stores/api"; // Adjust the correct path
import shipmentsStore from "../../stores/useStore";

const ShipmentsFilter = () => {
  const [users, setUsers, customers, setCustomers] = shipmentsStore((state) => [
    state.users,
    state.setUsers,
    state.customers,
    state.setCustomers,
  ]);

  const shipmentStatuses = [
    { value: "Shipped", label: "شُحنت" },
    { value: "Delivered", label: "تم التسليم" },
    { value: "Late", label: "متأخرة" },
    { value: "Feedback", label: "تحتاج إلى مراجعة" },
  ];

  const [selectedStatuses, setSelectedStatuses] = useState({
    Shipped: false,
    Delivered: false,
    Late: false,
    Feedback: false,
  });

  // دالة لتحديث حالة مربعات الاختيار بناءً على التغيير
  const handleStatusChange = (e) => {
    const { value, checked } = e.target; // القيمة وحالة الاختيار

    // تحديث حالة الاختيارات
    setSelectedStatuses((prevStatuses) => ({
      ...prevStatuses,
      [value]: checked, // تغيير حالة العنصر الذي تم تغييره فقط
    }));
  };

  // const [selectedUsers, setSelectedUsers] = useState([]);
  // const handleSelectedUsers = (e) => {
  //   const user = e.target.value;

  //   setSelectedUsers((prevStatuses) => ({
  //     ...prevStatuses,
  //     user, // تغيير حالة العنصر الذي تم تغييره فقط
  //   }));
  // };

  useEffect(() => {
    fetchUsers().then(setUsers); // Fetch users and update the store
  }, [setUsers]);

  useEffect(() => {
    fetchCustomers().then(setCustomers); // Fetch customers and update the store
  }, [setCustomers]);

  return (
    <div className="user-id-status-container">
      <h3>المستخدمين</h3>

      {/* {users.map((user) => (
        <div
          key={user.id}
          className="btn-group mb-2 mx-1"
          role="group"
          aria-label="Basic checkbox toggle button group"
          style={{ width: "100px" }}
        >
          <input
            type="checkbox"
            className="btn-check"
            value={user.value}
            id={`btncheck${user.id}`}
            autoComplete="off"
          />
          <label
            className="btn btn-outline-primary btn-sm"
            htmlFor={`status${user.id}`}
            style={{ width: "100px", textAlign: "center" }}
          >
            {user.first_name}
          </label>
        </div>
      ))} */}

      <div>
        {users.map((user) => (
          <div key={user.id}>
            <div
              className="btn-group mb-2 mx-1"
              role="group"
              aria-label="Basic checkbox toggle button group"
              style={{ width: "100px" }}
            >
              <input
                className="form-check-input"
                type="checkbox"
                value=""
                id={`flexCheckDefault${user.id}`}
              />
              <label className="form-check-label" htmlFor="flexCheckDefault">
                {user.first_name}
              </label>
            </div>
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
        {shipmentStatuses.map((status) => (
          <div
            key={status.value}
            className="btn-group mb-2 mx-1"
            role="group"
            aria-label="Basic checkbox toggle button group"
            style={{ width: "100px" }}
          >
            <input
              type="checkbox"
              className="btn-check"
              value={status.value}
              id={`status${status.value}`}
              autoComplete="off"
              onChange={handleStatusChange}
              checked={selectedStatuses[status.value]}
            />
            <label
              className="btn btn-outline-primary btn-sm"
              htmlFor={`status${status.value}`}
              style={{ width: "100px", textAlign: "center" }}
            >
              {status.label}
            </label>
          </div>
        ))}
      </div>

      <h3>التاريخ</h3>
      <h3>حالة الشحنة</h3>
    </div>
  );
};

export default ShipmentsFilter;
