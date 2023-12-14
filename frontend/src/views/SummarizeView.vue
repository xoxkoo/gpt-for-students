<template>
	<div class="container mt-20 mx-auto">
		<div class="flex flex-col align-center">
			<p class="text-sm">{{ $t('summarize.uploadYourFile') }}</p>
			<UploadBox v-if="!summarizedResponse.length" @on-upload="onFileUpload" />

			<div v-else>
				<Panel class="mt-10" :header="$t('summarize.responseHeader')">
					<p class="m-0" v-html="summarizedResponse"></p>
					<template #header>
						<Button :label="$t('summarize.buttonReupload')" icon="pi pi-check" @click="summarizedResponse = ''" />
					</template>
					<template #footer>
						<Button :label="$t('summarize.buttonReupload')" icon="pi pi-check" @click="summarizedResponse = ''" />
					</template>
				</Panel>
			</div>

			<InputText
				v-model="inputValue"
				@submit="onInputSubmit()"
				:placeholder="$t('summarize.inputPlaceholder')"
				type="text"
				size="large"
				class="mt-10"
			/>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
// import { fileService } from '../services/fileService';
import { chatService } from '../services/chatService';
import { removeSpecialChar } from '../utils/inputUtils';
import UploadBox from '../components/UploadBox.vue';
const inputValue = ref<string>('');
const summarizedResponse = ref<string>('');
// const fileUploaded = ref(true);

const onInputSubmit = () => {
	chatService.postQuestion(removeSpecialChar(inputValue.value));
};
const onFileUpload = (response: string) => {
	summarizedResponse.value = response;
};
</script>
