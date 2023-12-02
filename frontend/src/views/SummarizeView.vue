<template>
	<div class="container mt-20 mx-auto">
		<div class="flex flex-col align-center">
			<p class="text-sm">{{ $t('summarize.uploadYourFile') }}</p>
			<UploadBox @upload="onFileUpload" />

			<InputText
				v-model="inputValue"
				@submit="onInputSubmit()"
				:placeholder="$t('summarize.inputPlaceholder')"
				type="text"
				size="large"
				class="mt-20"
			/>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { fileService } from '../services/fileService';
import { chatService } from '../services/chatService';
import { removeSpecialChar } from '../utils/inputUtils';
import UploadBox from '../components/UploadBox.vue';
const inputValue = ref<string>('');
const fileUploaded = ref(true);

const onInputSubmit = () => {
	chatService.postQuestion(removeSpecialChar(inputValue.value));
};
const onFileUpload = (file: any) => {
	console.log('fileUploaded');
	console.log(file);

	// summarizationService.getWithQuery(removeSpecialChar(inputValue.value));
};
</script>
../services/fileService
