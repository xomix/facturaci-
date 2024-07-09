import axios from 'axios';

const state = {
  appartments: null,
  appartment: null
};

const getters = {
  stateAppartments: state => state.appartments,
  stateAppartment: state => state.appartment,
};

const actions = {
  async createAppartment({dispatch}, appartment) {
    await axios.post('appartments', appartment);
    await dispatch('getAppartments');
  },
  async getAppartments({commit}) {
    let {data} = await axios.get('appartments');
    commit('setAppartments', data);
  },
  async viewAppartment({commit}, id) {
    let {data} = await axios.get(`appartment/${id}`);
    commit('setAppartment', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateAppartment({}, appartment) {
    await axios.patch(`appartment/${appartment.id}`, appartment.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteAppartment({}, id) {
    await axios.delete(`appartment/${id}`);
  }
};

const mutations = {
  setAppartments(state, appartments){
    state.appartments = appartments;
  },
  setAppartment(state, appartment){
    state.appartment = appartment;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};