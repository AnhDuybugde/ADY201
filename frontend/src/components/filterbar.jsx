import api from '../utils/api';

const getPhones = async () => {
  const res = await api.get('/phones');
  console.log(res.data);
};
