<template>
	<Toast />
	<div class="card">
		<FileUpload
			name="file"
			:url="`${ENDPOINT_URL}file_handler/`"
			mode="advanced"
			:auto="true"
			@upload="onUpload"
			@error="onError"
			:multiple="false"
			accept=".pdf"
			:maxFileSize="1048576"
			:cancelLabel="$t('cancel')"
			:chooseLabel="$t('choose')"
			:uploadLabel="$t('upload')"
		>
			<template #empty>
				<p>{{ $t('dragAndDropFiles') }}</p>
			</template>
		</FileUpload>
	</div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { ENDPOINT_URL, TOAST_LIFE } from '../utils/constants';
import { useToast } from 'primevue/usetoast';
// import { errors } from '../../../errors.json';
// type ErrorResponse = keyof typeof errors;

const toast = useToast();
const { t } = useI18n();
const emits = defineEmits(['onUpload']);

const onUpload = (response: any) => {
	// TODO remake this as service
	if (response.xhr.status == 200) {
		const responseText = response.xhr.response;
		emits('onUpload', responseText);
	}
};
const onError = (response: any) => {
	toast.add({
		severity: 'error',
		summary: t('toast.error'),
		detail: t(`summarize.error.${response.xhr.status}`),
		life: TOAST_LIFE,
	});
};
</script>
