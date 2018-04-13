import React, { Component } from 'react';
import { render } from 'react-dom';
import changeCase from 'change-case';

const fieldContainerClass = `field-${window.foreignformField}`;
const fieldContainer = document.getElementsByClassName(fieldContainerClass)[0];

const placeHolder = (
  <div>
    <label className="required">
      {changeCase.sentenceCase(window.foreignformField)}:
    </label>
    <p>
      Save this model with a <b>
        {changeCase.sentenceCase(window.foreignformForeignKey)}
      </b> value to get additional form fields.
    </p>
  </div>
);

render(placeHolder, fieldContainer);
