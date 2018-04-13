import React, { Component } from 'react';
import { render } from 'react-dom';
import changeCase from 'change-case';
import Form from 'react-jsonschema-form';

import '../scss/change.scss';

const field = document.getElementsByName(window.foreignformField)[0];
const fieldContainerClass = `field-${window.foreignformField}`;
const fieldContainer = document.getElementsByClassName(fieldContainerClass)[0];
fieldContainer.style = 'display: none;';

const formApp = (
  <div>
    <div className="form-row field-name">
      <label className="required">
        {changeCase.sentenceCase(window.foreignformField)}:
      </label>
    </div>
    <Form
      className="foreignform"
      schema={window.foreignformJSONSchema || {}}
      uiSchema={window.foreignformUISchema || {}}
      formData={JSON.parse(field.value)}
      onChange={(form) => {
        field.value = JSON.stringify(form.formData);
      }}
      liveValidate
    />
  </div>
);

render(formApp, document.getElementById('foreignform'));
