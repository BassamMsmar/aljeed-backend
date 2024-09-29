import { create } from "zustand";



const shipmentsStore = create((set) => ({
  shipments: [],
  users: [],
  customers: [],
  shipmentStatus: [],
  filters:{
    selectedUsers: [],
    selectedStatuses:  [],
    selectedCustomers: [],
  },

  setShipments: (shipments) => set({ shipments }),
  setUsers: (users) => set({ users }),
  setCustomers: (customers) => set({ customers }),
  setShipmentStatus: (shipmentStatus) => set({ shipmentStatus }),
  setFilters: (filters) => set(state => ({filters : {...state.filters , ...filters}}))
}));

export default shipmentsStore;
