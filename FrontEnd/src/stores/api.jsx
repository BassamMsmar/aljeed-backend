import axios from "axios";

const API_URL = "http://127.0.0.1:8000/shipment/api";

export const fetchShipments = async () => {
  const response = await axios.get(`${API_URL}/list`);
  return response.data;
};
