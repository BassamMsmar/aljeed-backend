import { create } from 'zustand'

const shipmentsStore = create(set => ({
  shipments: [],

  setShipments: (shipments) => set({ shipments }),
  
}));

export default shipmentsStore;
 