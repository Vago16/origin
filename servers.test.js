describe("Servers test (with setup and tear-down)", function() {
  beforeEach(function () {
    // initialization logic
    serverNameInput.value = 'Alice';
  });

  it('should add a new server to allServers on submitServerInfo()', function () {
    submitServerInfo();

    expect(Object.keys(allServers).length).toEqual(1);
    expect(allServers['server' + serverId].serverName).toEqual('Alice');
  });

  it('Create table row element and updateServerTable', function () {
    updateServerTable();
    submitServerInfo();

    let serverTableList = document.querySelector('#serverTable tbody tr td')

    expect(serverTableList.length).toEqual(3);
    expect(serverTableList[0].innerText).toEqual('Alice');
    expect(serverTableList[1].innerText).toEqual('$0.00');
    expect(serverTableList[2].innerText).toEqual('X');
  });

  afterEach(function() {
    // teardown logic
    serverId = 0;
    serverTbody.innerHTML = '';
    allServers = {};
  });
});
