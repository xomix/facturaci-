import { createStore } from "vuex";

import users from './modules/users';
import appartments from "./modules/appartments";

export default createStore({
  modules: {
    users,
    appartments,
  }
});