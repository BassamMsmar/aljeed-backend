import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const fetchShipments = async (filters) => {
  try {
    const user = filters.selectedUsers.join(',')
    const customer = filters.selectedCustomers.join(',')
    const status = filters.selectedStatuses.join(',')
    
    
    const params = {
      user:user,
      customer:customer,
      status:status,
    }
    console.log(params)

    const response = await axios.get(`${API_URL}/shipment/api/list/`, {params});
    // console.log(response.data)
    return response.data;
  } catch (error) {
    console.error("Error fetching shipments:", error);
    return []; // Return an empty array or handle it as needed
  }
};

export const fetchUsers = async () => {
  try {
    const response = await axios.get(`${API_URL}/user/api/list/`);

    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
    return []; // Return an empty array or handle it as needed
  }
};

export const fetchStatus = async () => {
  const response = await axios.get(`${API_URL}/shipment/api/shipment_status/`);
  return response.data;
};

export const fetchCustomers = async () => {
  const response = await axios.get(`${API_URL}/customer/api/branch/`);
  return response.data;
};
