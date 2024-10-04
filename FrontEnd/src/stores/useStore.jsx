import { create } from "zustand";

const shipmentsStore = create((set) => ({
  shipments: [],
  users: [],
  customers: [],
  shipmentStatus: [],
  filters: {
    selectedUsers: [],
    selectedCustomers: [],
    selectedStatuses: [],
  },

  setShipments: (shipments) => set({ shipments }),
  setUsers: (users) => set({ users }),
  setCustomers: (customers) => set({ customers }),
  setShipmentStatus: (shipmentStatus) => set({ shipmentStatus }),

  setFilters: (filters) =>
    set((state) => ({ filters: { ...state.filters, ...filters } })),
}));

export default shipmentsStore;
