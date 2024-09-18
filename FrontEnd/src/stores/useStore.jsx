import { create } from "zustand";



const shipmentsStore = create((set) => ({
  shipments: [],
  users: [],
  drivers: [],
  customers: [],
  status: [
    { value: "Shipped", label: "شُحنت" },
    { value: "Delivered", label: "تم التسليم" },
    { value: "Late", label: "متأخرة" },
    { value: "Feedback", label: "تحتاج إلى مراجعة" },
  ],

  setShipments: (shipments) => set({ shipments }),
  setUsers: (users) => set({ users }),
  setDrivers: (drivers) => set({ drivers }),
  setCustomers: (customers) => set({ customers }),
  setShipmentStatuses: (shipmentStatuses) => set({ shipmentStatuses }),
}));

export default shipmentsStore;
