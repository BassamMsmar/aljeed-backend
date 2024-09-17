import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const fetchShipments = async () => {
  const response = await axios.get(`${API_URL}shipment/api/list`);
  return response.data;
};

export const fetchUsers = async () => {
  const response = await axios.get(`${API_URL}/user/api/list/`);
  return response.data;
};

export const fetchStatus = async () => {
  const response = await axios.get(`${API_URL}/list`);
  return response.data;
};

export const fetchCustomers = async () => {
  const response = await axios.get(`${API_URL}/list`);
  return response.data;
};
