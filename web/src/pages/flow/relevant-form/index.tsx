import LLMSelect from '@/components/llm-select';
import { useTranslate } from '@/hooks/commonHooks';
import { Form } from 'antd';
import { useSetLlmSetting } from '../hooks';
import { IOperatorForm } from '../interface';

const RelevantForm = ({ onValuesChange, form }: IOperatorForm) => {
  const { t } = useTranslate('chat');
  useSetLlmSetting(form);

  return (
    <Form
      name="basic"
      labelCol={{ span: 8 }}
      wrapperCol={{ span: 16 }}
      style={{ maxWidth: 600 }}
      initialValues={{ remember: true }}
      onValuesChange={onValuesChange}
      autoComplete="off"
      form={form}
    >
      <Form.Item
        name={'llm_id'}
        label={t('model', { keyPrefix: 'chat' })}
        tooltip={t('modelTip', { keyPrefix: 'chat' })}
      >
        <LLMSelect></LLMSelect>
      </Form.Item>
    </Form>
  );
};

export default RelevantForm;
