          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        {% for score in scores %}
          <tr>
            <td>{{ score.user.username }}</td>
            <td>{{ score.score }}</td>
          </tr>
        {% empty %}
          <tr>
            <td colspan="2">No scores available.</td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  {% else %}
    <p>No scores available.</p>
  {% endif %}
{% endblock %}
