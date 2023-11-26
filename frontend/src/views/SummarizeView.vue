<template>
	<div class="container mt-20 mx-auto">
		<InputText
			v-if="fileUploaded"
			v-model="inputValue"
			@submit="onInputSubmit()"
			:placeholder="$t('summarize.inputPlaceholder')"
			type="text"
			size="large"
			class="mx-auto"
		/>
		<UploadBox v-else @upload="onFileUpload" />
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { summarizationService } from '../services/summarizationService';
import { chatService } from '../services/chatService';
import { removeSpecialChar } from '../utils/inputUtils';
import UploadBox from '../components/UploadBox.vue';
const inputValue = ref<string>('');
const fileUploaded = ref(true);

const onInputSubmit = () => {
	chatService.postQuestion(removeSpecialChar(inputValue.value));
};
const onFileUpload = () => {
	summarizationService.getWithQuery(removeSpecialChar(inputValue.value));
};
</script>
