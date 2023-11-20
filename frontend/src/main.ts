import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import i18n from './i18n';
import Button from 'primevue/button';

import 'primeicons/primeicons.css';
import './assets/scss/tailwind.css';
import 'primevue/resources/themes/mira/theme.css';
import 'primevue/resources/primevue.min.css';
import './assets/scss/base.scss';

const app = createApp(App);

app.use(i18n);
app.use(createPinia());
app.use(router);

app.use(PrimeVue);
app.component('Button', Button);

app.mount('#app');
