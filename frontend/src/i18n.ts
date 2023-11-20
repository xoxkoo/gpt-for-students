import { createI18n } from 'vue-i18n';
import cz from './locales/cz';
import en from './locales/en';
import sk from './locales/sk';

const messages = {
	cz,
	sk,
	en,
};

const i18n = createI18n({
	legacy: false,
	locale: 'cz', // Default locale
	fallbackLocale: 'en',
	globalInjection: true,
	messages,
});

export default i18n;
