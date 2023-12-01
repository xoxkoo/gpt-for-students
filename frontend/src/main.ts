/* eslint-disable vue/no-reserved-component-names */
/* eslint-disable vue/multi-word-component-names */
import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import PrimeVue from 'primevue/config';
import i18n from './i18n';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import FileUpload from 'primevue/fileupload';
import ToastService from 'primevue/toastservice';

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
app.use(ToastService);
app.component('Button', Button);
app.component('FileUpload', FileUpload);
app.component('InputText', InputText);

app.mount('#app');
