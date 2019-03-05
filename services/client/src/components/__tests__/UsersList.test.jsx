import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';

import UsersList from '../UsersList';

const users = [
    {
        'active': true,
        'email': 'khanhnguyen@gmail.com',
        'id': 1,
        'username': 'khanh'
      },
      {
        'active': true,
        'email': 'thuhoang@gmail.com',
        'id': 2,
        'username': 'thu'
      }
];

test('UserList renders properly', () => {
    const wrapper = shallow(<UsersList users={users}/>);
    const element = wrapper.find('h4');
    expect(element.length).toBe(2);
    expect(element.get(0).props.children).toBe('khanh');
});

test('UserList renders a snapshot properly', () => {
    const tree = renderer.create(<UsersList users={users}/>).toJSON();
    expect(tree).toMatchSnapshot();
})