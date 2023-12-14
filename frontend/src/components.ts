/* eslint-disable vue/no-reserved-component-names */
/* eslint-disable vue/multi-word-component-names */
import { App } from 'vue';
import Button from 'primevue/button';
import Toast from 'primevue/toast';
import Panel from 'primevue/panel';
import FileUpload from 'primevue/fileupload';
import InputText from 'primevue/inputtext';

export default function registerComponents(app: App) {
	app.component('Button', Button);
	app.component('Toast', Toast);
	app.component('Panel', Panel);
	app.component('FileUpload', FileUpload);
	app.component('InputText', InputText);
}
