import { create } from "zustand";



const shipmentsStore = create((set) => ({
  shipments: [],
  users: [],
  customers: [],
  filters:{
    selectedStatuses: {
      Shipped: true,
      Delivered: true,
      Late: true,
      Feedback: true
    },
    selectedUsers: [],
    selectedCustomers: [],
  },

  setShipments: (shipments) => set({ shipments }),
  setUsers: (users) => set({ users }),
  setCustomers: (customers) => set({ customers }),
  setFilters: (filters) => set({ filters }),
}));

export default shipmentsStore;
